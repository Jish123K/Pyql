#include <iostream>

#include <vector>

#include <algorithm>

#include <cmath>

#include <SFML/Graphics.hpp>

using namespace std;

class MathProblemSolver {

public:

  MathProblemSolver() {}

  void solve(vector<int> numbers) {

    int answer = 0;

    for (int i = 0; i < numbers.size(); i++) {

      answer += numbers[i];

    }

    cout << "The answer is " << answer << endl;

  }

  void draw(sf::RenderWindow& window) {

    sf::Text text("The answer is 0", font, 20);

    text.setPosition(100, 100);

    window.draw(text);

  }

private:

  sf::Font font;

};

int main() {

  MathProblemSolver problemSolver;

  vector<int> numbers = {1, 2, 3, 4, 5};

  problemSolver.solve(numbers);

  sf::RenderWindow window(sf::VideoMode(800, 600), "Math Problem Solver");

  while (window.isOpen()) {

    sf::Event event;

    while (window.pollEvent(event)) {

      if (event.type == sf::Event::Closed) {

        window.close();

      }

    }

    window.clear();

    problemSolver.draw(window);

    window.display();

  }

  return 0;

}

