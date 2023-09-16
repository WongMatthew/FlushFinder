from db_system import DB

def main():
    with DB() as db_inst:
        db_inst.create_entry(3.5, "123 test st.", "all the time", active=True, review="test rev")
        washrooms = db_inst.get_entries()
        print(washrooms)
        db_inst.update_entry(washrooms[0].id, cleaniness=4.5) 

if __name__ == "__main__":
    main()