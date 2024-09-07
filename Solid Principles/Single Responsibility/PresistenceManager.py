import pickle
class PresistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename,"wb")
        pickle.dump(journal, file)
        # file.write(str(journal))
        file.close()

    @staticmethod
    def load_from_file(filename):
        file = open(filename,"rb")
        # journal = pickle.load(file)
        journal = pickle.load(file)
        print(journal)
        file.close()
        return journal