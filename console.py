"""
OSAD console
"""
import cmd
import sys
from models import db, app
from models.admins_model import Admin
from models.articals_model import Artical
from models.job_offers_model import JobOffer

class Console(cmd.Cmd):
    """
    Command line interbter for OASD application
    methods

        create: will create a new instance of [Admin | Artical | JobOffer]
        show: will dispaly information about instance
        edite: will edit an instance

    """

    prompt = '(OASD) '

    def do_quit(self, line):
        return True
    
    def emptyline(self, line):
        pass

    def do_create(self, line):
        """
        create      create a new model instance
        create <class name> <**kwargs>
        """
        cls, *args = line.split()

        new_instance = eval(cls)()
        for i in range(0, len(args)):
            arg = args[i]
            try:
                key, val = arg.split("=")
                if key == '' or val == '':
                    continue
                # if the value was string containing spaces
                if val.startswith('"') and not val.endswith('"'):
                    continue

                val = val.replace("_", " ")
                val = val.replace("\"", "")  # remove the qouts
                val = val.replace("'", "")  # remove the qouts

                print(f'setting {key} to {val}')
                if key == 'password':
                    new_instance.password = val
                else:
                    setattr(new_instance, key, val)
            except ValueError:
                pass
        print(new_instance.id)
        # exit()
        new_instance.save()

    def do_show(self, line):
        """
        show    display some information about an instance
        show <class name> <instance id> 
        """
        try:
            cls, id = line.split()
            instances = db.get(cls, filters=id)
        except ValueError:
            cls = eval(line.strip())
            with app.app_context():
                instances = db.session.execute(db.select(cls)).all()
        for instance in instances:
            print(instance)

    def do_delete(self, line):
        """
        delete    delete a record from database
        delete <class Name> <instance id>
        """
        try:
            cls, id = line.split()
            instance = db.get(cls, filters=id)[0]
            print(type(instance))
        except ValueError:
            print("Instance id missing")
        # except Exception as e:
        #     print(f"Database error: {e}")


if __name__ == "__main__":
    Console().cmdloop()