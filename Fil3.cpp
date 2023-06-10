#include <iostream>

#include <vector>

#include <algorithm>

#include <cmath>

#include <SFML/Graphics.hpp>

using namespace std;

class MathProblemSolver

{

public:

    MathProblemSolver() {}

    void Solve(int level)

    {

        // Generate a random math problem

        int num1 = rand() % 100;

        int num2 = rand() % 100;

        int operator1 = rand() % 4;

        // Create a vector of possible answers

        vector<int> answers;

        answers.push_back(num1 + num2);

        answers.push_back(num1 - num2);

        answers.push_back(num1 * num2);

        answers.push_back(num1 / num2);

        // Shuffle the answers

        random_shuffle(answers.begin(), answers.end());

        // Display the math problem

        cout << num1 << " " << operator1 << " " << num2 << endl;

        // Get the user's answer

        int userAnswer;

        cin >> userAnswer;

        // Check if the user's answer is correct

        bool correct = false;

        for (int answer : answers)

        {

            if (answer == userAnswer)

            {

                correct = true;

                break;

            }

        }

        // Display the result

        if (correct)

        {

            cout << "Correct!" << endl;

        }

        else

        {

            cout << "Incorrect. The answer is " << answers[0] << endl;

        }

    }

};

int main()

{

    // Create a window

    sf::RenderWindow window(sf::VideoMode(800, 600), "Math Problem Solver");

    // Create a math problem solver

    MathProblemSolver solver;

    // Start the main loop

    while (window.isOpen())

    {

        // Handle events

        sf::Event event;

        while (window.pollEvent(event))

        {

            // Close the window if the user clicks the close button

            if (event.type == sf::Event::Closed)

            {

                window.close();

            }

        }

        // Solve a math problem

        solver.Solve(rand() % 5);

        // Clear the window

        window.clear();

        // Draw the math problem solver

        solver.Draw(window);

        // Display the window

        window.display();

    }

    return 0;

}

