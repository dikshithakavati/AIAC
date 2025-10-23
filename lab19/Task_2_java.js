function checkNumber(num) {
    // Check if the number is positive, negative, or zero
    if (num > 0) {
        return "Positive";
    } else if (num < 0) {
        return "Negative";
    } else {
        return "Zero";
    }
}

// Test cases
console.log(checkNumber(5));    // Should print "Positive"
console.log(checkNumber(-3));   // Should print "Negative"
console.log(checkNumber(0));    // Should print "Zero"
