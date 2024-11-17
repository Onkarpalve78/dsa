package Codevita.clock;

import java.util.Scanner;

public class LearningWithClock2 {

    // Method to calculate the angle between the hour and minute hands
    public static double calculateAngle(int hour, int minute) {
        // Minute hand moves 6 degrees per minute
        double minuteAngle = minute * 6;

        // Hour hand moves 0.5 degrees per minute, plus 30 degrees per hour
        double hourAngle = (hour % 12) * 30 + minute * 0.5;

        // Find the absolute difference between the two angles
        double angle = Math.abs(hourAngle - minuteAngle);

        // Return the smaller of the two possible angles (interior or exterior)
        return Math.min(angle, 360 - angle);
    }

    // Method to calculate the minimum cost for each query
    public static int calculateCost(double currentAngle, int targetAngle, int A, int B, int X, int Y) {
        // Calculate the angle difference
        double angleDiff1 = Math.abs(currentAngle - targetAngle);
        double angleDiff2 = 360 - angleDiff1;

        // Calculate costs for minute hand (clockwise and counterclockwise)
        int minuteCostCw = (int) (angleDiff1 * Y * A); // Moving clockwise for minute hand
        int minuteCostCcw = (int) (angleDiff1 * Y * B); // Moving counter-clockwise for minute hand
        int minuteCostCwAlt = (int) (angleDiff2 * Y * A); // Alternative clockwise for minute hand
        int minuteCostCcwAlt = (int) (angleDiff2 * Y * B); // Alternative counter-clockwise for minute hand

        // Calculate costs for hour hand (clockwise and counterclockwise)
        int hourCostCw = (int) (angleDiff1 * X * A); // Moving clockwise for hour hand
        int hourCostCcw = (int) (angleDiff1 * X * B); // Moving counter-clockwise for hour hand
        int hourCostCwAlt = (int) (angleDiff2 * X * A); // Alternative clockwise for hour hand
        int hourCostCcwAlt = (int) (angleDiff2 * X * B); // Alternative counter-clockwise for hour hand

        // Return the minimum cost to adjust both hands
        return Math.min(
                Math.min(Math.min(minuteCostCw, minuteCostCcw), Math.min(minuteCostCwAlt, minuteCostCcwAlt)),
                Math.min(Math.min(hourCostCw, hourCostCcw), Math.min(hourCostCwAlt, hourCostCcwAlt)));
    }

    // Method to calculate the total minimum cost for all queries
    public static int totalMinimumCost(String initialTime, int Q, int A, int B, int X, int Y, int[] queries) {
        // Extract the hour and minute from the initial time
        String[] timeParts = initialTime.split(":");
        int hour = Integer.parseInt(timeParts[0]);
        int minute = Integer.parseInt(timeParts[1]);

        // Calculate the initial angle between the hour and minute hands
        double currentAngle = calculateAngle(hour, minute);

        // Variable to hold the total cost
        int totalCost = 0;

        // Process each query
        for (int i = 0; i < Q; i++) {
            int targetAngle = queries[i];

            // Calculate the cost to adjust the hands to form the target angle
            int cost = calculateCost(currentAngle, targetAngle, A, B, X, Y);

            // Add the cost to the total cost
            totalCost += cost;
        }

        return totalCost;
    }

    public static void main(String[] args) {
        // Scanner to read input
        Scanner sc = new Scanner(System.in);

        // Reading the initial time
        String initialTime = sc.nextLine().trim();

        // Reading the number of queries
        int Q = Integer.parseInt(sc.nextLine().trim());

        // Reading A, B, X, and Y
        String[] costs = sc.nextLine().split(" ");
        int A = Integer.parseInt(costs[0]);
        int B = Integer.parseInt(costs[1]);
        int X = Integer.parseInt(costs[2]);
        int Y = Integer.parseInt(costs[3]);

        // Reading the queries
        int[] queries = new int[Q];
        for (int i = 0; i < Q; i++) {
            queries[i] = Integer.parseInt(sc.nextLine().trim());
        }

        // Calculating the total minimum cost for all queries
        int result = totalMinimumCost(initialTime, Q, A, B, X, Y, queries);

        // Output the result
        System.out.println(result);

        // Closing the scanner
        sc.close();
    }
}
