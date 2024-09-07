from Journal import Journal
from PresistenceManager import PresistenceManager


j = Journal()
j.add_entry("Journal One")
j.add_entry("Journal Two")
# j.display()
# j.remove_entry(0)
j.display()
PresistenceManager().save_to_file(j,"journal.txt")
journal = PresistenceManager.load_from_file("journal.txt")
print(journal.entries)