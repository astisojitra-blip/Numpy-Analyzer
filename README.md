# Advanced NumPy Data Analyzer

**Author:** Asti Sojitra  
**Programming Language:** Python  
**Core Library:** NumPy  
**Programming Paradigm:** Object-Oriented Programming (OOP)  
**Application Type:** Menu-Driven Command-Line Application

## 1. Project Overview

Advanced NumPy Data Analyzer is a Python console application designed to create and analyze numerical arrays. It brings together multidimensional array handling, mathematical calculations, searching, sorting, filtering, and statistical analysis through an interactive menu system. The application uses NumPy for array processing and a `DataAnalytics` class to organize its features.

## 2. Project Objectives

- Practice NumPy operations on one-dimensional, two-dimensional, and three-dimensional arrays.
- Apply object-oriented programming concepts to a practical Python project.
- Make common numerical operations accessible through menus rather than requiring users to write commands.
- Display array transformations and calculated results clearly in the terminal.

## 3. Technologies Used

| Technology | Purpose |
| --- | --- |
| Python 3.14.6 | Application logic and command-line interaction |
| NumPy | Multidimensional arrays, calculations, and statistics |
| Visual Studio Code (VS Code) | Used for writing, editing, and running Python code. |
| Git | Used for version control and tracking changes in the project code. |
| GitHub | Used for storing, managing, and sharing the project repository |

## 4. Object-Oriented Design

The program is organized around the `DataAnalytics` class.

- **Private instance variable:** `self.__arr` stores the current array.
- **Constructor:** `__init__()` initializes the array state to `None`.
- **Class method:** `welcome()` displays the starting message.
- **Static method:** `show_message()` displays the exit message.
- **Private helper methods:** `__check_array()` checks whether an array has been created, and `__calculate_sum()` returns its sum. These helpers are defined but are not called by the current menus.
- **Instance methods:** Separate methods handle array creation, indexing, arithmetic, combining, searching, and statistics.

## 5. Project Structure

The project follows a simple, single-file Python structure. A suggested folder layout is shown below:

```text
NumPy Analyzer/
├── main.py
└── README.md
└── output.png
```

- **main.py:** Contains the `DataAnalytics` class, array operations, interactive submenus, and the main application loop.
- **README.md:** Contains project documentation, setup instructions, and usage information.

All functional modules are methods within the main Python program rather than separate files.

## 6. Main Features

### 6.1 Array Creation and Reshaping

Users can create three types of integer NumPy arrays:

- **1D arrays:** A single sequence of values.
- **2D arrays:** Values arranged into rows and columns.
- **3D arrays:** Values arranged into blocks, rows, and columns.

The program accepts space-separated integer inputs. For 2D and 3D arrays, `reshape()` arranges the entered elements into the requested dimensions.

### 6.2 Indexing and Slicing

After creating an array, users can open the indexing and slicing menu.

- **Indexing:** Retrieves an element by its position, using one index for 1D, two for 2D, and three for 3D arrays.
- **Slicing:** Extracts a range of elements using `start:end` notation, with separate ranges for each dimension when needed.

### 6.3 Mathematical Operations

The mathematical menu supports:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

For addition, subtraction, division, and non-2D multiplication, the program asks for a second array with the same shape and performs element-wise calculations. For **2D multiplication**, it instead uses `np.dot()` to perform matrix multiplication, with the second matrix's row count determined by the first matrix's column count.

### 6.4 Combining and Splitting Arrays

- **Vertical stacking:** `np.vstack()` combines the current array with another array of the same shape.
- **Array splitting:** `np.array_split()` divides the current array into a user-selected number of sections along the first axis. Sections may have unequal sizes.

### 6.5 Searching, Sorting, and Filtering

- **Searching:** `np.where()` locates a specified value and displays its index coordinates.
- **Ascending sorting:** `np.sort(..., axis=-1)` sorts values along the last axis.
- **Descending sorting:** Reverses the ascending result along the last axis using `[..., ::-1]`.
- **Filtering:** Boolean indexing selects values greater than a user-entered threshold.

Both sorting orders are displayed during the same sorting operation. In multidimensional arrays, sorting is performed along the last axis rather than globally across every element.

### 6.6 Aggregate and Statistical Analysis

The statistics menu provides the following calculations:

| Operation | NumPy Function | Description |
| --- | --- | --- |
| Sum | `np.sum()` | Total of all elements |
| Mean | `np.mean()` | Arithmetic average |
| Median | `np.median()` | Middle value of sorted data |
| Standard deviation | `np.std()` | Spread of values around the mean |
| Variance | `np.var()` | Average squared deviation from the mean |
| Minimum | `np.min()` | Smallest element |
| Maximum | `np.max()` | Largest element |
| Percentile | `np.percentile()` | Value at a selected percentile |
| Correlation coefficient | `np.corrcoef()` | Correlation matrix between two flattened arrays |

The percentile option accepts a numeric percentile from 0 to 100. The correlation option asks for a second array of the same shape and flattens both arrays before calculating the correlation matrix.

## 7. Command-Line Menu Structure

The main menu presents six choices:

```text
1. Create a NumPy Array
2. Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter
5. Aggregates and Statistics
6. Exit
```

Each operation group has its own submenu, and the **Go Back** option returns to the main menu. Users can perform multiple operations during one session.


## 8. Installation and Setup

Python and NumPy are required to run the application.

Install the NumPy library using the following command:

```bash
pip install numpy
```

## 9. How to Run

1. Save the Python program as `main.py` (or use its actual filename).
2. Open a terminal in the directory containing the file.
3. Run the program:

   ```bash
   python main.py
   ```

4. Choose **1** to create an array before selecting analysis operations.
5. Enter integer elements separated by spaces, then select the desired menu option.
6. Choose **6** from the main menu to exit.

## 10. Example Usage

The following example illustrates sorting a 1D array containing five values:

```text
Original Array:
[30 10 50 20 40]

Ascending Order:
[10 20 30 40 50]

Descending Order:
[50 40 30 20 10]
```

For a percentile calculation, entering `50` requests the 50th percentile, which corresponds to the median of the array.

## 11. Input and Output Behavior

The application uses `input()` to receive menu choices, dimensions, array elements, indices, ranges, and calculation parameters. It converts array elements to integers and prints NumPy arrays directly to the console. Most calculations produce new result arrays or values; the original stored array is not replaced by those results.

## 12. Current Limitations

- Invalid text entered where an integer is expected can raise `ValueError`.
- An incorrect number of elements can cause `reshape()` to fail.
- Out-of-range indices can raise `IndexError`.
- Analysis options do not currently call `__check_array()`, so choosing them before array creation can cause errors.
- The 2D creation prompt says **“Enter 6 elements”** even when the user selects other dimensions.
- The `n` value entered during 1D creation is not used to verify the element count.
- Division by zero is not explicitly handled.
- Correlation may produce undefined (`NaN`) results for constant input arrays.

## 13. Learning Outcomes

This project demonstrates practical use of NumPy's multidimensional arrays, array indexing, slicing, broadcasting-compatible element-wise operations, matrix multiplication, stacking, splitting, Boolean filtering, and descriptive statistics. It also provides experience with Python classes, methods, loops, conditionals, and menu-based console programming.

## 14. Conclusion

Advanced NumPy Data Analyzer combines important numerical operations in a single interactive Python application. It is a useful educational project for practicing NumPy and object-oriented programming, while providing a foundation for future improvements in input validation, data handling, and analytical functionality.
