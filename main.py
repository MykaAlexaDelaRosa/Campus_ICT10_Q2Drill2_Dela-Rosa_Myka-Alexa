from pyscript import document #display 

# Members from each grade
grade7 = {"Alex Cruz", "Rose Garcia", "Leo Ramos", "Mia Santos"}
grade8 = {"Sam Reyes", "Ella Flores", "Noah Reyes", "Kate Lim"}
grade9 = {"Liam Torres", "Sofia Mendoza", "Ethan Ramos", "Chloe Rivera"}
grade10 = {"Daniel Flores", "Ava Castillo", "Nathan Garcia"}

# Combine all members into one set
club_members = grade7 | grade8 | grade9 | grade10

# Add a new member
def add_member(event):
    first_name = document.querySelector("#first").value.strip()
    last_name = document.querySelector("#last").value.strip()
    full_name = first_name + " " + last_name

    # Add the new name to the set
    club_members.update({full_name})

    # Make a bullet list of all members
    member_list = "".join(f"<li>{name}</li>" for name in sorted(club_members))

    # Display the members and total
    document.querySelector("#result").innerHTML = f"""
        <h3>ICT Club Members</h3>
        <ul style="text-align: left;">{member_list}</ul>
        <h4>Total Members: {len(club_members)}</h4>
    """
