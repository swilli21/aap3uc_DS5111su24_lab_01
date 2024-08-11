#src/pkg_aap3uc/__main__.py

from . import functions  # Import your module(s)

def main():
    # Place the code you want to execute here
    print("Running pkg_aap3uc package!")
    result = add_one(1)  # Call a function from your package
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
