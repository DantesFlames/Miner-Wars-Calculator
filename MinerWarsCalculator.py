# MIT License
# Copyright (c) 2024 DantesFlames
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as tk

# Initialize counters and risk level
total_gmt_cost = 0
total_dollar_cost = 0
total_purple_count = 0
total_red_count = 0

def calculate_contributions():
    global total_dollar_cost
    try:
        # Retrieve input values
        clan_share = float(entry_clan_share.get()) / 100  # Convert to decimal
        block_reward = float(entry_block_reward.get())
        block_multiplier = float(entry_block_multiplier.get())  # Block reward multiplier
        gmt_value = float(entry_gmt_value.get())
        
        # Adjust block reward by multiplier and calculate the user's share of it
        adjusted_block_reward = block_reward * block_multiplier
        your_reward = adjusted_block_reward * clan_share

        # Calculate the break-even GMT contribution based on reward share only
        break_even_gmt = round(your_reward / gmt_value)

        # Calculate recommended contributions based on risk tolerance
        high_risk_gmt = round(break_even_gmt * 0.6)  # 60% of break-even
        moderate_risk_gmt = round(break_even_gmt * 0.3)  # 30% of break-even
        low_risk_gmt = round(break_even_gmt * 0.1)  # 10% of break-even

        # Determine tally color based on risk level
        if total_gmt_cost >= high_risk_gmt:
            tally_color = "red"
        elif total_gmt_cost >= moderate_risk_gmt:
            tally_color = "orange"
        else:
            tally_color = "green"

        # Display results with the specified colors
        result_label.config(text=f"Break-Even GMT Contribution: {break_even_gmt} GMT", fg="white")
        high_risk_label.config(text=f"High Risk (60% of Break-Even): {high_risk_gmt} GMT", fg="red")
        moderate_risk_label.config(text=f"Moderate Risk (30% of Break-Even): {moderate_risk_gmt} GMT", fg="orange")
        low_risk_label.config(text=f"Low Risk (10% of Break-Even): {low_risk_gmt} GMT", fg="green")
        reminder_label.config(text="**Remember, you only receive a reward if the clan wins**", fg="white")

        # Update dollar cost based on current total GMT and input GMT value
        total_dollar_cost = round(total_gmt_cost * gmt_value, 2)
        update_cost_display(tally_color)
    except ValueError:
        result_label.config(text="Error: Please enter valid numeric values.", fg="white")
        high_risk_label.config(text="")
        moderate_risk_label.config(text="")
        low_risk_label.config(text="")
        reminder_label.config(text="")

def add_purple():
    global total_gmt_cost, total_purple_count
    total_gmt_cost += 9
    total_purple_count += 1
    calculate_contributions()

def add_red():
    global total_gmt_cost, total_red_count
    total_gmt_cost += 1
    total_red_count += 1
    calculate_contributions()

def clear_counters():
    global total_gmt_cost, total_dollar_cost, total_purple_count, total_red_count
    total_gmt_cost = 0
    total_dollar_cost = 0
    total_purple_count = 0
    total_red_count = 0
    update_cost_display("white")

def update_cost_display(tally_color):
    gmt_cost_label.config(text=f"Total GMT Cost: {total_gmt_cost} GMT", fg=tally_color)
    dollar_cost_label.config(text=f"Total Dollar Cost: ${total_dollar_cost}", fg=tally_color)
    purple_tally_label.config(text=f"Total Purple: {total_purple_count}", fg=tally_color)
    red_tally_label.config(text=f"Total Red: {total_red_count}", fg=tally_color)

# Set up the main application window with darker purple background and white text
root = tk.Tk()
root.title("Risk-Based GMT Contribution Calculator")
root.geometry("1200x800")
root.configure(bg="#2e1a47")  # Darker purple background

# Counter Section at Top Center
counter_frame = tk.Frame(root, bg="#2e1a47")
counter_frame.grid(row=0, column=1, padx=20, pady=20)

tk.Label(counter_frame, text="Cost Counter", font=('Arial', 14, 'bold'), bg="#2e1a47", fg="white").pack(pady=5)
gmt_cost_label = tk.Label(counter_frame, text="Total GMT Cost: 0 GMT", font=('Arial', 12), bg="#2e1a47", fg="white")
gmt_cost_label.pack(pady=5)

dollar_cost_label = tk.Label(counter_frame, text="Total Dollar Cost: $0", font=('Arial', 12), bg="#2e1a47", fg="white")
dollar_cost_label.pack(pady=5)

purple_tally_label = tk.Label(counter_frame, text="Total Purple: 0", font=('Arial', 12), bg="#2e1a47", fg="white")
purple_tally_label.pack(pady=5)

red_tally_label = tk.Label(counter_frame, text="Total Red: 0", font=('Arial', 12), bg="#2e1a47", fg="white")
red_tally_label.pack(pady=5)

# Buttons to add Purple and Red contributions
tk.Button(counter_frame, text="Add Purple (9 GMT)", command=add_purple, bg="#2e1a47", fg="white").pack(pady=5)
tk.Button(counter_frame, text="Add Red (1 GMT)", command=add_red, bg="#2e1a47", fg="white").pack(pady=5)
tk.Button(counter_frame, text="Clear Counters", command=clear_counters, bg="#2e1a47", fg="white").pack(pady=5)

# Entry Fields and Results in Top Right
entry_frame = tk.Frame(root, bg="#2e1a47")
entry_frame.grid(row=0, column=2, padx=20, pady=20, sticky="ne")

tk.Label(entry_frame, text="Clan Share Percentage:", bg="#2e1a47", fg="white").pack(pady=5)
entry_clan_share = tk.Entry(entry_frame)
entry_clan_share.pack(pady=5)

tk.Label(entry_frame, text="Block Reward Value (any currency):", bg="#2e1a47", fg="white").pack(pady=5)
entry_block_reward = tk.Entry(entry_frame)
entry_block_reward.pack(pady=5)

tk.Label(entry_frame, text="Block Reward Multiplier:", bg="#2e1a47", fg="white").pack(pady=5)
entry_block_multiplier = tk.Entry(entry_frame)
entry_block_multiplier.pack(pady=5)

tk.Label(entry_frame, text="Value per GMT (same currency as Block Reward):", bg="#2e1a47", fg="white").pack(pady=5)
entry_gmt_value = tk.Entry(entry_frame)
entry_gmt_value.pack(pady=5)

# Calculate button
calculate_button = tk.Button(entry_frame, text="Calculate Recommended Contribution", command=calculate_contributions, bg="white", fg="#2e1a47")
calculate_button.pack(pady=20)

# Result labels with different risk tolerance colors
result_label = tk.Label(entry_frame, text="", font=('Arial', 12), bg="#2e1a47", fg="white")
result_label.pack(pady=5)

high_risk_label = tk.Label(entry_frame, text="", font=('Arial', 12), bg="#2e1a47")
high_risk_label.pack(pady=5)

moderate_risk_label = tk.Label(entry_frame, text="", font=('Arial', 12), bg="#2e1a47")
moderate_risk_label.pack(pady=5)

low_risk_label = tk.Label(entry_frame, text="", font=('Arial', 12), bg="#2e1a47")
low_risk_label.pack(pady=5)

# Reminder label
reminder_label = tk.Label(entry_frame, text="", font=('Arial', 10), bg="#2e1a47", fg="white")
reminder_label.pack(pady=10)

# Instructions and Disclaimer Section at Bottom Center
info_frame = tk.Frame(root, bg="#2e1a47")
info_frame.grid(row=1, column=1, columnspan=2, pady=20)

instructions = """
Instructions:
1. Enter your Clan Share Percentage (e.g., 3.4 for 3.4%).
   Clan Share % can be found at https://app.gomining.com/nft-pool
2. Enter the Block Reward Value in any currency.
3. Enter the Block Reward Multiplier (e.g., 8 for an 8x reward).
4. Enter the Value per GMT in the same currency as the Block Reward.
5. Click "Calculate Recommended Contribution" to see the break-even GMT and recommended GMT amounts based on different risk levels.
"""
instructions_label = tk.Label(info_frame, text=instructions, font=('Arial', 10), justify='left', bg="#2e1a47", fg="white")
instructions_label.pack(pady=10)

disclaimer = """
Disclaimer:
This is a test program. Use it at your own risk. The information provided by this
program is not financial advice. Always make informed decisions based on your unique circumstances.
"""
disclaimer_label = tk.Label(info_frame, text=disclaimer, font=('Arial', 8), fg="white", bg="#2e1a47", justify='left')
disclaimer_label.pack(pady=10)

# Run the application
root.mainloop()
