import streamlit as st
from logic import calculate  # Direct import—same folder

# Rest of your code stays the same
# Page config
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

def main():
    st.title("🧮 Simple Calculator")
    st.markdown("Enter numbers and select an operation below.")

    # Sidebar for inputs
    st.sidebar.header("Inputs")
    num1 = st.sidebar.number_input("First Number", value=0.0, step=0.1)
    num2 = st.sidebar.number_input("Second Number", value=0.0, step=0.1)
    operation = st.sidebar.selectbox("Select Operation", ["+", "-", "*", "/", "^", "sqrt"])

    if st.sidebar.button("Compute"):
        try:
            result = calculate(num1, num2, operation)
            st.success(f"**Result: {result:.2f}**")

            # Show the calculation expression
            if operation == "sqrt":
                st.info(f"√{num1} = {result:.2f}")
            else:
                st.info(f"{num1} {operation} {num2} = {result:.2f}")

        except ValueError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"Unexpected Error: {e}")

    # Footer
    st.markdown("---")
    st.markdown("*Built with logic.py + Streamlit*")

if __name__ == "__main__":
    main()