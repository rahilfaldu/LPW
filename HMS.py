class Patient:
    def __init__(self, name, age, ailment):
        self.name = name
        self.age = age
        self.ailment = ailment

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, age, ailment):
        new_patient = Patient(name, age, ailment)
        self.patients.append(new_patient)
        print("Patient added successfully.")

    def view_patients(self):
        if not self.patients:
            print("No patients found.")
            return
        print("List of Patients:")
        for patient in self.patients:
          print("Name, Age: , Ailment: ")

def main():
    hms = HospitalManagementSystem()
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient's name: ")
            age = input("Enter patient's age: ")
            ailment = input("Enter patient's ailment: ")
            hms.add_patient(name, age, ailment)
        elif choice == '2':
            hms.view_patients()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()






