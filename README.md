# Remove Duplicate Elements

## Explanation

This program removes duplicate values from a list.

## Problem Statement

Write a Python program to remove duplicate elements while keeping the first occurrence of each value.

## Features

* Accepts a list
* Detects duplicate values
* Removes duplicates
* Preserves original order

## How It Works

A set is used to keep track of values already encountered. A separate list stores the unique values.

## Technologies Used

* Python 3

## Data Structure Used

* List
* Set

## Methods Used

* `input()`
* `split()`
* `set()`
* `append()`

## Program Flow

1. Read the list
2. Create an empty set
3. Check each element
4. Add unseen elements
5. Display the unique list

## Sample Input

```text
1 2 2 3 4 4 5
```

## Sample Output

```text
List without duplicates: [1, 2, 3, 4, 5]
```

## Time Complexity

O(n) average case

## Space Complexity

O(n)

## Key Learning

* Lists
* Sets
* Duplicate detection
* Data organization

## File Location

`remove_duplicates.py`

## Repository Structure

```text
python-remove-duplicates/
├── remove_duplicates.py
└── README.md
```

## Author

V.Harini
