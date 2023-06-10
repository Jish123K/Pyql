#include <iostream>

#include <vector>

#include <algorithm>

#include <cmath>

#include <SDL.h>

using namespace std;

const int WINDOW_WIDTH = 800;

const int WINDOW_HEIGHT = 600;

struct Point {

  int x;

  int y;

};

struct Line {

  Point start;

  Point end;

};

void render(SDL_Renderer* renderer) {

  // Clear the screen

  SDL_RenderClear(renderer);

  // Draw the lines

  for (Line line : lines) {

    SDL_RenderDrawLine(renderer, line.start.x, line.start.y, line.end.x, line.end.y);

  }

  // Update the screen

  SDL_RenderPresent(renderer);

}

void handle_events(SDL_Event* event) {

  switch (event->type) {

    case SDL_QUIT:

      // Quit the application

      cout << "Quitting..." << endl;

      SDL_Quit();

      exit(0);

      break;

    case SDL_MOUSEBUTTONDOWN:

      // Add a new line to the list

      Point point;

      point.x = event->button.x;

      point.y = event->button.y;

      lines.push_back({point, point});

      break;

  }

}

int main() {

  // Initialize SDL

  SDL_Init(SDL_INIT_VIDEO);

  // Create a window

  SDL_Window* window = SDL_CreateWindow("Math Problem Solver", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_SHOWN);

  // Create a renderer

  SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

  // Create a list of lines

  vector<Line> lines;

  // Start the event loop

  while (true) {

    // Handle events

    SDL_Event event;

    while (SDL_PollEvent(&event)) {

      handle_events(&event);

    }

    // Render the lines

    render(renderer);

  }

  // Quit SDL

  SDL_Quit();

  return 0;

}

