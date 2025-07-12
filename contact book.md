import tkinter as tk
from tkinter import messagebox, simpledialog

# Global contact list
contacts = []

# Add new contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    
    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    clear_entries()
    update_contact_list()
    messagebox.showinfo("Success", "Contact added!")

# Display all contacts
def update_contact_list():
    contact_list.delete(0, tk.END)
    for index, contact in enumerate(contacts):
        contact_list.insert(tk.END, f"{index + 1}. {contact['name']} - {contact['phone']}")

# Clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Search contact by name or phone
def search_contact():
    query = search_entry.get().strip().lower()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Update selected contact
def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a contact to update.")
        return
    index = selected[0]
    contact = contacts[index]

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    contact['name'] = name
    contact['phone'] = phone
    contact['email'] = email
    contact['address'] = address

    update_contact_list()
    messagebox.showinfo("Success", "Contact updated!")

# Delete selected contact
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a contact to delete.")
        return
    index = selected[0]
    contacts.pop(index)
    update_contact_list()
    clear_entries()
    messagebox.showinfo("Deleted", "Contact deleted!")

# Load selected contact into fields
def on_select(event):
    selected = contact_list.curselection()
    if not selected:
        return
    index = selected[0]
    contact = contacts[index]
    name_entry.delete(0, tk.END)
    name_entry.insert(0, contact["name"])
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact["phone"])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, contact["email"])
    address_entry.delete(0, tk.END)
    address_entry.insert(0, contact["address"])

# GUI setup
root = tk.Tk()
root.title("📇 Contact Manager")
root.geometry("500x500")

# Entry frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(entry_frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(entry_frame, text="Phone:").grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(entry_frame, width=30)
phone_entry.grid(row=1, column=1)

tk.Label(entry_frame, text="Email:").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(entry_frame, width=30)
email_entry.grid(row=2, column=1)

tk.Label(entry_frame, text="Address:").grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(entry_frame, width=30)
address_entry.grid(row=3, column=1)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Contact", command=add_contact, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update Contact", command=update_contact, width=15).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Contact", command=delete_contact, width=15).grid(row=0, column=2, padx=5)

# Search bar
search_entry = tk.Entry(root, width=40)
search_entry.pack(pady=5)
tk.Button(root, text="Search", command=search_contact).pack()

# Contact listbox
contact_list = tk.Listbox(root, width=60)
contact_list.pack(pady=10)
contact_list.bind('<<ListboxSelect>>', on_select)

update_contact_list()

root.mainloop()
