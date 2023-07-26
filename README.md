# Flower Procedural Modeling
This is a simple Python application to demonstrate how grammars are used in procedural modeling. The application provides a GUI implemented using the Tkinter library.

## Installation on Linux
1. Clone or download the repository `git clone https://github.com/vercah/procedural-modeling.git`
2. Go to the project directory `cd procedural-modeling`
3. Install the library, if needed `apt-get install python-tk` (you might need sudo)
4. Run the application `python3 flower-generator.py`

## Usage
In the left panel, there are 4 fields for the grammar rules. `A` represents stem, `B` left leaf, `C` right leaf, and `D` is the flower. Square brackets `[]` represent left branch, round brackets `()` is the right branch. You can specify the number of substitution iterations the program performs. Once you click `Submit`, the flower starts to appear. You can use `Meadow` to show some examples of how it might look like.

## Brief description of the code
The code uses strings as grammars and processes them char by char. It goes through the given number of iterations in a for loop and creates the final grammar. Then it modifies the grammar so it is a simple one (i. e., fixes expressions such as `a(ab)(ac)` to `a(abac)`) and draws all the flower parts using the chars from the final grammar. If the input includes unknown signs, the program ignores them.

