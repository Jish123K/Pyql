import java.awt.*;

import java.awt.event.*;

import java.util.Scanner;

public class MathSolver {

    private static final int WINDOW_WIDTH = 300;

    private static final int WINDOW_HEIGHT = 200;

    private Frame frame;

    private Label label;

    private TextField textField;

    private Button addButton, subtractButton, multiplyButton, divideButton;

    private TextArea outputArea;

    public MathSolver() {

        frame = new Frame("Math Solver");

        frame.setSize(WINDOW_WIDTH, WINDOW_HEIGHT);

        frame.setLayout(new FlowLayout());

        label = new Label("Enter a number:");

        textField = new TextField(10);

        addButton = new Button("Add");

        subtractButton = new Button("Subtract");

        multiplyButton = new Button("Multiply");

        divideButton = new Button("Divide");

        outputArea = new TextArea(10, 30);

        frame.add(label);

        frame.add(textField);

        frame.add(addButton);

        frame.add(subtractButton);

        frame.add(multiplyButton);

        frame.add(divideButton);

        frame.add(outputArea);

        addButton.addActionListener(new ActionListener() {

            @Override

            public void actionPerformed(ActionEvent e) {

                int num1 = Integer.parseInt(textField.getText());

                int num2 = Scanner.nextInt();

                int result = num1 + num2;

                outputArea.setText(num1 + " + " + num2 + " = " + result);

            }

        });

        subtractButton.addActionListener(new ActionListener() {

            @Override

            public void actionPerformed(ActionEvent e) {

                int num1 = Integer.parseInt(textField.getText());

                int num2 = Scanner.nextInt();

                int result = num1 - num2;

                outputArea.setText(num1 + " - " + num2 + " = " + result);

            }

        });

        multiplyButton.addActionListener(new ActionListener() {

            @Override

            public void actionPerformed(ActionEvent e) {

                int num1 = Integer.parseInt(textField.getText());

                int num2 = Scanner.nextInt();

                int result = num1 * num2;

                outputArea.setText(num1 + " * " + num2 + " = " + result);

            }

        });

        divideButton.addActionListener(new ActionListener() {

            @Override

            public void actionPerformed(ActionEvent e) {

                int num1 = Integer.parseInt(textField.getText());

                int num2 = Scanner.nextInt();

                int result = num1 / num2;

                outputArea.setText(num1 + " / " + num2 + " = " + result);

            }

        });

        frame.setVisible(true);

    }

    public static void main(String[] args) {

        new MathSolver();

    }

}

