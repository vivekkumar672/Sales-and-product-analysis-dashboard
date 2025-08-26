import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# ----------------------------
# Sample Data
# ----------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [1200000, 1500000, 1800000, 1300000, 1700000, 2100000,
         2000000, 2200000, 1900000, 2500000, 2700000, 3000000]
orders = [1000, 1200, 1400, 1100, 1350, 1600,
          1550, 1650, 1500, 1800, 1900, 2100]

regions = {"North": 4500000, "South": 3800000, "East": 3000000, "West": 5500000}
categories = {"Electronics": 5000000, "Clothing": 3500000,
              "Groceries": 4200000, "Home & Living": 2800000, "Sports": 2300000}

# ----------------------------
# Tkinter Window
# ----------------------------
root = tk.Tk()
root.title("📊 Sales & Product Analysis Dashboard")
root.geometry("1400x800")

# --- Top KPIs ---
frame_kpi = tk.Frame(root, bg="lightblue", height=80)
frame_kpi.pack(fill="x")

lbl1 = tk.Label(frame_kpi, text="💰 Monthly Revenue: ₹17,690,936.94", font=("Arial", 14, "bold"), bg="lightblue")
lbl2 = tk.Label(frame_kpi, text="📦 Monthly Orders: 14,990", font=("Arial", 14, "bold"), bg="lightblue")
lbl3 = tk.Label(frame_kpi, text="🛒 Avg Order Value: ₹1,180.18", font=("Arial", 14, "bold"), bg="lightblue")

lbl1.pack(side="left", padx=40, pady=20)
lbl2.pack(side="left", padx=40, pady=20)
lbl3.pack(side="left", padx=40, pady=20)

# --- Main Split (Left = Sales, Right = Product) ---
frame_main = tk.Frame(root)
frame_main.pack(fill="both", expand=True)

frame_left = tk.Frame(frame_main)
frame_left.pack(side="left", fill="both", expand=True)

frame_right = tk.Frame(frame_main)
frame_right.pack(side="right", fill="both", expand=True)

# ----------------------------
# LEFT PANEL (Sales Summary)
# ----------------------------
tk.Label(frame_left, text="📈 Sales Summary", font=("Arial", 16, "bold")).pack()

# Sales Trend (Bar Chart)
fig1, ax1 = plt.subplots(figsize=(4, 3))
ax1.bar(months, sales, color="royalblue")
ax1.set_title("Sales Trend")
canvas1 = FigureCanvasTkAgg(fig1, master=frame_left)
canvas1.get_tk_widget().pack()

# Orders Trend (Line Chart)
fig2, ax2 = plt.subplots(figsize=(4, 3))
ax2.plot(months, orders, marker="o", color="green")
ax2.set_title("Order Trend")
canvas2 = FigureCanvasTkAgg(fig2, master=frame_left)
canvas2.get_tk_widget().pack()

# Regional Sales Contribution (Pie Chart)
fig3, ax3 = plt.subplots(figsize=(4, 3))
ax3.pie(regions.values(), labels=regions.keys(), autopct="%1.1f%%")
ax3.set_title("Regional Sales Contribution")
canvas3 = FigureCanvasTkAgg(fig3, master=frame_left)
canvas3.get_tk_widget().pack()

# ----------------------------
# RIGHT PANEL (Product Analysis)
# ----------------------------
tk.Label(frame_right, text="📦 Product Analysis", font=("Arial", 16, "bold")).pack()

# Sales by Category (Bar Chart)
fig4, ax4 = plt.subplots(figsize=(4, 3))
ax4.bar(categories.keys(), categories.values(), color="orange")
ax4.set_title("Sales by Category")
canvas4 = FigureCanvasTkAgg(fig4, master=frame_right)
canvas4.get_tk_widget().pack()

# Category Share (Donut Chart)
fig5, ax5 = plt.subplots(figsize=(4, 3))
wedges, texts, autotexts = ax5.pie(categories.values(), labels=categories.keys(),
                                   autopct="%1.1f%%", pctdistance=0.85)
centre_circle = plt.Circle((0, 0), 0.70, fc="white")
fig5.gca().add_artist(centre_circle)
ax5.set_title("Category Share (Donut)")
canvas5 = FigureCanvasTkAgg(fig5, master=frame_right)
canvas5.get_tk_widget().pack()

# Item Details (Table)
tree = ttk.Treeview(frame_right, columns=("Category", "Sales"), show="headings", height=5)
tree.heading("Category", text="Category")
tree.heading("Sales", text="Sales")
for cat, val in categories.items():
    tree.insert("", "end", values=(cat, f"₹{val:,}"))
tree.pack(pady=10, fill="x")

# ----------------------------
root.mainloop()
