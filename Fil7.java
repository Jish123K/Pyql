import java.awt.*;

import java.awt.event.*;

import java.util.StringTokenizer;

public class MathProblemSolver extends Frame {

    private Button addButton, subtractButton, multiplyButton, divideButton;

    private Label inputLabel, outputLabel;

    private TextField inputTextField, outputTextField;

    public MathProblemSolver() {

        super("Math Problem Solver");

        addButton = new Button("Add");

        subtractButton = new Button("Subtract");

        multiplyButton = new Button("Multiply");

        divideButton = new Button("Divide");

        inputLabel = new Label("Enter two numbers: ");

        outputLabel = new Label("Result: ");

        inputTextField = new TextField(10);

        outputTextField = new TextField(10);

        addButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {

                StringTokenizer st = new StringTokenizer(inputTextField.getText());

                double num1 = Double.parseDouble(st.nextToken());

                double num2 = Double.parseDouble(st.nextToken());

                double result = num1 + num2;

                outputTextField.setText(String.valueOf(result));

            }

        });

        subtractButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {

                StringTokenizer st = new StringTokenizer(inputTextField.getText());

                double num1 = Double.parseDouble(st.nextToken());

                double num2 = Double.parseDouble(st.nextToken());

                double result = num1 - num2;

                outputTextField.setText(String.valueOf(result));

            }

        });

        multiplyButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {

                StringTokenizer st = new StringTokenizer(inputTextField.getText());

                double num1 = Double.parseDouble(st.nextToken());

                double num2 = Double.parseDouble(st.nextToken());

                double result = num1 * num2;

                outputTextField.setText(String.valueOf(result));

            }

        });

        divideButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {

                StringTokenizer st = new StringTokenizer(inputTextField.getText());

                double num1 = Double.parseDouble(st.nextToken());

                double num2 = Double.parseDouble(st.nextToken());

                double result = num1 / num2;

                outputTextField.setText(String.valueOf(result));

            }

        });

        Panel buttonPanel = new Panel();

        buttonPanel.add(addButton);

        buttonPanel.add(subtractButton);

        buttonPanel.add(multiplyButton);

        buttonPanel.add(divideButton);

        Panel inputPanel = new Panel();

        inputPanel.add(inputLabel);

        inputPanel.add(inputTextField);

        Panel outputPanel = new Panel();

        outputPanel.add(outputLabel);

        outputPanel.add(outputTextField);

        getContentPane().add(buttonPanel, BorderLayout.SOUTH);

        getContentPane().add(inputPanel, BorderLayout.CENTER);

        getContentPane().add(outputPanel, BorderLayout.NORTH);

        setSize(300, 100);

        setVisible(true);

    }

    public static void main(String[] args) {

        new MathProblemSolver();

    }

}

