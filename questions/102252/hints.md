
# Question 102252

**Question Title**: Train

**Question Link**: [Train](https://quera.org/problemset/102252) 

**Difficulty Level**: 🟢
## Question Description
The Train class is already implemented, but you have to implement the Trip and Passenger classes.



## Key Points
- using Dunder Methods

## Sample Code
```python
def __call__(self):
        total_weight = sum([p.load_weight for p in self.passengers])
        remaining_weight_capacity = self.train.weight_capacity - total_weight
        return remaining_weight_capacity
```

## Status


- **Completed**

## Learning
- [Dunder Methods](./../../learn/dunder_methods.md)