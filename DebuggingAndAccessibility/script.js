// Assume you have some JavaScript code that needs debugging
function calculateTotal(price, quantity) {
    // Example of a buggy function
    return price * quanity; // Note the misspelling of 'quantity'
}

// Debugging using console.log()
function calculateTotal(price, quantity) {
    console.log('Price:', price);
    console.log('Quantity:', quantity);
    // Corrected spelling of 'quantity'
    return price * quantity;
}

// Debugging using breakpoints in Chrome DevTools
// Open Chrome DevTools, navigate to Sources tab, find your JavaScript file
// Click on the line number to set a breakpoint
// Refresh the page and debugger will pause execution at that line

// Debugging using Firefox Developer Tools
// Similar to Chrome DevTools, open Firefox DevTools and navigate to Debugger tab
// Set breakpoints by clicking on the line number

// These methods allow you to inspect variables, step through code, and identify issues