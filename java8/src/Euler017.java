import framework.EulerProblem;

import java.util.function.IntPredicate;
import java.util.stream.IntStream;

/**
 * If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
 * 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 * <p>
 * If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
 * letters would be used?
 */
public class Euler017 extends EulerProblem<Integer> {

    @Override
    public long solve(Integer maxCount) {
        return IntStream.rangeClosed(1, maxCount)
                .mapToObj(British::numberToText)
                .mapToLong(Euler017::countLetters)
                .sum();
    }

    private static long countLetters(String input) {
        return countMatches(input, Character::isAlphabetic);
    }

    private static long countMatches(String input, IntPredicate predicate) {
        return input.chars()
                .filter(predicate)
                .count();
    }
}

class British {
    private final static String[] ones =
            {"", "one", "two", "three", "four",
                    "five", "six", "seven", "eight", "nine"};

    private final static String[] teens =
            {"ten", "eleven", "twelve", "thirteen", "fourteen",
                    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};

    private final static String[] tens =
            {"", "", "twenty", "thirty", "forty",
                    "fifty", "sixty", "seventy", "eighty", "ninety"};

    private final static String hundred = "hundred";
    private final static String thousand = "thousand";
    private final static String afterHundreds = " and ";
    private final static String afterTens = "-";

    public static String numberToText(int n) {
        if (n <= 0 || n >= 10_000) {
            throw new IllegalArgumentException("Only positive integers up to 10,000 allowed");
        }

        StringBuilder sb = new StringBuilder();

        int thousands = n / 1000;
        if (thousands > 0) {
            sb.append(ones[thousands]).append(" ").append(thousand);
            n = n % 1000;
            if (n > 0) {
                sb.append(" ");
            }
        }

        int hundreds = n / 100;
        if (hundreds > 0) {
            sb.append(ones[hundreds]).append(" ").append(hundred);
            n = n % 100;
            if (n > 0) {
                sb.append(afterHundreds);
            }
        }

        if (n >= 10 && n < 20) {
            sb.append(teens[n - 10]);
            n = 0;
        }

        int ten = n / 10;
        if (ten > 0) {
            sb.append(tens[ten]);
            n = n % 10;
            if (n > 0) {
                sb.append(afterTens);
            }
        }

        sb.append(ones[n]);

        return sb.toString();
    }
}
