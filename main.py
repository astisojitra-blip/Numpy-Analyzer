
import numpy as np

class DataAnalytics:
    def __init__(self):
        self.__arr = None
        
        
    #class method
    @classmethod
    def welcome(cls):
        print("\nwelcome to the Numpy Analyzer!")
        print("=========================================")
        
    # static method
    @staticmethod
    def show_message():
        print("Thank you for using Numpy Analyzer!")
        
    # Private method: check whether an array exists
    def __check_array(self):
        if self.__arr is None:
            print("Please create an array first")
            return False
        return True
    
    #Private method: calculate sum
    def __calculate_sum(self):
        return np.sum(self.__arr)
    
    
    # Create 1D, 2D or 3D array
    def create_array(self):
        while True:
            print("Select the type of array to create:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
    
            choice = int(input("Enter your choice: "))
        
            if choice == 1:
                n = int(input("Enter number of elements: "))
                arr = np.array(list(map(int,input("Enter elements: ").split())))
                self.__arr = arr

                print("1D Array:", self.__arr)
                self.indexing_slicing_menu()
        
            elif choice == 2:
                rows = int(input("Enter the number of rows: "))
                columns = int(input("Enter the number of columns:"))
                arr = np.array(list(map(int,input("Enter 6 elements for the array separated by space: ").split())))
            
                arr = arr.reshape(rows, columns)

                self.__arr = arr
                print("Array created Successfully:")
                print(self.__arr)
                self.indexing_slicing_menu()
            
            elif choice == 3:
                depth = int(input("Enter the number of blocks: "))
                rows = int(input("Enter the number of rows: "))
                columns = int(input("Enter the number of columns: "))
                arr = np.array(list(map(int,input("Enter elements for the array separated by space: ").split()))) 
                arr = arr.reshape(depth,rows,columns) 
                self.__arr = arr
                print("array created successfully:")
                print(self.__arr)
                self.indexing_slicing_menu()
                break  
            
    def indexing_slicing_menu(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                # 1D array
                if self.__arr.ndim == 1:
                    idx = int(input("Enter index: "))
                    print("Element:", self.__arr[idx]) 
                     
                
                # 2D array
                elif self.__arr.ndim == 2:
                    r = int(input("Enter row index: "))
                    c = int(input("Enter column index: "))
                    print("Element:", self.__arr[r, c])
                    
                # 3D array 
                elif self.__arr.ndim == 3:
                    b = int(input("Enter block index: "))
                    r = int(input("Enter row index: "))
                    c = int(input("Enter column index: "))
                    print("Element:", self.__arr[b, r, c])
                    
            elif choice == 2: 
                    # 1D array slicing
                if self.__arr.ndim == 1:
                    r = input("Enter the range (start:end): ")
                    start, end = map(int, r.split(':'))
                    print("Sliced Array:", self.__arr[start:end])
                
                # 2D array slicing
                elif self.__arr.ndim == 2:
                    r = input("Enter the row range (start:end): ")
                    c = input("Enter the column range (start:end): ")
                    r_start, r_end = map(int, r.split(':'))
                    c_start, c_end = map(int, c.split(':'))
                    print("Sliced Array:\n", self.__arr[r_start:r_end, c_start:c_end])
                
                # 3D array slicing
                elif self.__arr.ndim == 3:
                    b = input("Enter the block range (start:end): ")
                    r = input("Enter the row range (start:end): ")
                    c = input("Enter the column range (start:end): ")
                    b_start, b_end = map(int, b.split(':'))
                    r_start, r_end = map(int, r.split(':'))
                    c_start, c_end = map(int, c.split(':'))
                    print("Sliced Array:\n", self.__arr[b_start:b_end, r_start:r_end, c_start:c_end])
                 
            elif choice == 3:
                break
                       
    def maths(self):
        while True:
            print("\nChoose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Go Back")
            
            choice = int(input("Enter your choice: "))
            
            if choice in [1, 2, 3, 4]:
                size = self.__arr.size
                shape = self.__arr.shape
                
                
                if choice == 3 and self.__arr.ndim == 2:
                    cols = shape[1]
                    rows2 = cols
                    cols2 = int(input(f"Enter number of columns for second array (rows will be {rows2}): "))
                    elements = list(map(int, input(f"Enter {rows2 * cols2} elements separated by space: ").split()))
                    arr2 = np.array(elements).reshape((rows2, cols2))
                    
                    print("\nOriginal Array:")
                    print(self.__arr)
                    print("\nSecond Array:")
                    print(arr2)
                    
                    result = np.dot(self.__arr, arr2)
                    print("\nResult of Matrix Multiplication:")
                    print(result)
                else:
                    
                    elements = list(map(int, input(f"Enter the same-size array elements ({size} elements separated by space): ").split()))
                    arr2 = np.array(elements).reshape(shape)
                    
                    print("\nOriginal Array:")
                    print(self.__arr)
                    print("\nSecond Array:")
                    print(arr2)
                    
                    if choice == 1:
                        result = self.__arr + arr2
                        print("\nResult of Addition:")
                    elif choice == 2:
                        result = self.__arr - arr2
                        print("\nResult of Subtraction:")
                    elif choice == 3:
                        result = self.__arr * arr2
                        print("\nResult of Multiplication:")
                    elif choice == 4:
                        result = self.__arr / arr2
                        print("\nResult of Division:")
                        
                    print(result)
                    
            elif choice == 5:
                break  
            else:
                print("Invalid choice! Try again.")
                
    def combine_split(self):
        while True:
            print("\nCombine or Split Arrays:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                size = self.__arr.size
                shape = self.__arr.shape
                
                elements = list(map(int, input(f"Enter the elements of another array to combine ({size} elements separated by space): ").split()))
                arr2 = np.array(elements).reshape(shape)
                
                print("\nOriginal Array:")
                print(self.__arr)
                
                print("\nSecond Array:")
                print(arr2)
                
        
                combined = np.vstack((self.__arr, arr2))
                print("\nCombined Array (Vertical Stack):")
                print(combined)
                
            elif choice == 2:
                print("\nOriginal Array:")
                print(self.__arr)
                
                sections = int(input("Enter the number of sections to split: "))
              
                    
                split_result = np.array_split(self.__arr, sections)
                print("\nSplit Arrays Result:")
                print(split_result)
                     
            elif choice == 3:
                break
            else:
                print("Invalid choice! Try again.")
                
    def search_sort_filter(self):
        while True:
            print("\nChoose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            print("4. Go Back")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                val = int(input("Enter value to search: "))
                indices = np.where(self.__arr == val)
                
                print("\nOriginal Array:")
                print(self.__arr)
                
                if len(indices[0]) > 0:
                    print(f"\nValue {val} found at indices:", list(zip(*indices)))
                else:
                    print(f"\nValue {val} not found in the array.")
                    
            elif choice == 2:
                print("\nOriginal Array:")
                print(self.__arr)
            
                ascending_arr = np.sort(self.__arr, axis=-1)
                descending_arr = ascending_arr[..., ::-1]

                print("\nAscending Order:")
                print(ascending_arr)

                print("\nDescending Order:")
                print(descending_arr)
                print("(Sorting applied row-wise.)")
                
            elif choice == 3:
                val = int(input("Enter condition value (greater than): "))
                filtered_arr = self.__arr[self.__arr > val]
                
                print("\nOriginal Array:")
                print(self.__arr)
                print(f"\nValues greater than {val}:")
                print(filtered_arr)
                
            elif choice == 4:
                break
            else:
                print("Invalid choice! Try again.")
                
    def Aggregates_Statistics(self):
        while True:
            print("\nAggregates and Statistics:")
            print("Choose an aggregate/statistical operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum and Maximum")
            print("7. Percentile")
            print("8. Correlation Coefficient")
            print("9. Go Back")
            
            choice = int(input("Enter your choice: "))
            
            if choice in [1, 2, 3, 4, 5, 6, 7]:
                print("\nOriginal Array:")
                print(self.__arr)
                
                if choice == 1:
                    result = np.sum(self.__arr)
                    print("Sum of Array:",result)
                elif choice == 2:
                    result = np.mean(self.__arr)
                    print("Mean of Array:",result)
                elif choice == 3:
                    result = np.median(self.__arr)
                    print("Median of Array:",result)
                elif choice == 4:
                    result = np.std(self.__arr)
                    print("Standard Deviation of Array:",result)
                elif choice == 5:
                    result = np.var(self.__arr)
                    print("Variance of Array:",result)
                elif choice == 6:
                    print("Minimum Value:",np.min(self.__arr))
                    print("Maximum Value:",np.max(self.__arr))
                elif choice == 7:
                    p = float(input("Enter percentile (e.g., 50 for median): "))
                    result = np.percentile(self.__arr, p)
                    print(f"Percentile {p:g} of Array:", result)
                    
            elif choice == 8:
                print("\nOriginal Array:")
                print(self.__arr)
                size = self.__arr.size
                shape = self.__arr.shape
                elements = list(map(int, input(f"Enter elements for second array ({size} elements separated by space): ").split()))
                arr2 = np.array(elements).reshape(shape)
                
                print("\nSecond Array:")
                print(arr2)
                
                # Correlation coefficient matrix calculate karva mate
                corr = np.corrcoef(self.__arr.flatten(), arr2.flatten())
                print("\nCorrelation Coefficient Matrix:")
                print(corr)
                
            elif choice == 9:
                break
            else:
                print("Invalid choice! Try again.")
def main():
    obj = DataAnalytics()
    obj.welcome()   

    while True:
        print("1. Create a NumPy Array")
        print("2. Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort or Filter")
        print("5. Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            obj.create_array()
        elif choice == "2":
            obj.maths()
        elif choice == "3":
            obj.combine_split()
        elif choice == "4":
            obj.search_sort_filter()
        elif choice == "5":
            obj.Aggregates_Statistics()
        elif choice == "6":
            obj.show_message()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

        