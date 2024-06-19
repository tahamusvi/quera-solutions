
# Question 60134

**Question Title**: Fruit chess

**Question Link**: [Fruit chess](https://quera.org/problemset/60134) 

**Difficulty Level**: 🟢
## Question Description
Karim Kachel is a professional chess player of the neighborhood who quarantined himself at home after the Corona situation. But unfortunately, he lost his chess pieces and due to the situation of Corona, he cannot order the pieces from outside and decided to make the pieces with the fruits he has at home. He understands that he cannot use any fruit as a chess piece and only good fruits can be used as a chess piece.

## Approach
- Nested Functions or Inner Functions in Python

## Key Points
- Nested functions are functions defined within other functions.
- Nested functions have access to variables from the enclosing (outer) function's scope, creating a closure.
- Nested functions can help with encapsulation, readability, and flexibility of the code.
- Nested functions are a powerful technique in Python, allowing you to organize related functionality and leverage the benefits of closures.

## Sample Code
```python
def outer_function(arg1, arg2):
    def inner_function(x):
        # inner_function has access to variables from outer_function's scope
        return x + arg1 + arg2
    
    # You can call inner_function from outer_function
    result = inner_function(10)
    return result

output = outer_function(5, 7)
print(output)  # Output: 22
```

In the above example, `inner_function` is a nested function that has access to the `arg1` and `arg2` variables from the `outer_function` scope. This demonstrates the concept of a closure, where an inner function can access variables from the enclosing function.

## Additional Resources
- [Python's Nested Functions and Closures](https://realpython.com/python-closure/)
- [Python Nested Functions: An In-Depth Explanation](https://www.freecodecamp.org/news/python-nested-functions-explained/)
- [Closures in Python: A Deeper Dive](https://www.toptal.com/python/python-closures-an-introduction)
- [Python Closures and Nested Functions](https://www.geeksforgeeks.org/python-closures-and-nested-functions/)

These resources provide more in-depth explanations and examples of nested functions and closures in Python, which can be helpful for understanding the concepts used in the `fruits` function you provided earlier.


## Status

- **Completed**


