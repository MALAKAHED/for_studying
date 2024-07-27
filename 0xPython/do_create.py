# old do_creat 
def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()
        
# new do creat 
def do_create(self, args):
        """ Create an object of any class"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # Create a dictionary to hold the attribute-value pairs
        attr_dict = {}
        for param in args_list[1:]:
            key_value = param.split('=')
            if len(key_value) == 2:
                key, value = key_value
                # Handle string
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('_', ' ').replace('\\"', '"')
                    attr_dict[key] = value
                # Handle float
                elif '.' in value:
                    try:
                        value = float(value)
                        attr_dict[key] = value
                    except ValueError:
                        pass
                # Handle int
                else:
                    try:
                        value = int(value)
                        attr_dict[key] = value
                    except ValueError:
                        pass

        new_instance = HBNBCommand.classes[class_name]()
        for key, value in attr_dict.items():
            setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)
