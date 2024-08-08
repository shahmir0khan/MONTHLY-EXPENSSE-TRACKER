# Expense Tracker Application

This application is a simple expense tracker built using Python's `tkinter` library for the graphical user interface (GUI). It allows users to add, list, search, and generate reports for their expenses, and stores the data in a JSON file.

## Features

- **Add Expense**: Allows users to input and save their expenses, including the product name, category, amount, and date.
- **List Expenses**: Displays a list of expenses either for a specific category or all categories.
- **Search Expense**: Searches and displays expenses by the product name.
- **Generate Report**: Generates a report of expenses for a specific month and year.
- **Exit**: Exits the application.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/expense-tracker.git
    ```
2. **Navigate to the directory**:
    ```bash
    cd expense-tracker
    ```
3. **Install the required dependencies**:
    - Ensure you have Python installed.
    - Install required libraries:
    ```bash
    pip install Pillow
    ```

## Usage

1. **Run the application**:
    ```bash
    python expense_tracker.py
    ```
2. **Add an expense**:
    - Click on the "Add Expense" button.
    - Fill in the details for product name, category, amount, and date.
    - Click on "Add Expense" to save the expense.
    
3. **List expenses**:
    - Click on the "List Expenses" button.
    - Enter a specific category or type "all" to list all expenses.
    - A new window will display the expenses.
    
4. **Search for an expense**:
    - Click on the "Search Expense" button.
    - Enter the product name.
    - A new window will display the expenses that match the search criteria.
    
5. **Generate a report**:
    - Click on the "Generate Report" button.
    - Enter the month and year.
    - A report for the specified period will be generated and displayed.

6. **Exit the application**:
    - Click on the "Exit" button to close the application.

## File Structure

- **expense_tracker.py**: Main script containing the application's logic.
- **exp_file1.json**: JSON file where all expenses are stored.
- **bg.jpeg**: Background image for the main window.
- **calculator-icon_34473 (1).ico**: Icon for the application windows.

## Dependencies

- **Python 3.x**
- **tkinter**: Standard Python interface to the Tk GUI toolkit.
- **Pillow**: Python Imaging Library (PIL Fork) for image processing.

## License

This project is licensed under the MIT License. 

## Acknowledgments

- **tkinter** for providing the GUI components.
- **Pillow** for handling images within the application.

---

Feel free to customize and enhance this README based on your specific project needs!
