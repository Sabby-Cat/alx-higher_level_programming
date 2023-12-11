#!/usr/bin/python3
"""base class"""
import json
import csv
import turtle


class Base:
    """base object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """creates json str"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json str to file"""
        file = cls.__name__ + ".json"
        with open(file, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dict_list = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """creates dict from json str"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create class from dict attr"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                ret = cls(1, 1)
            else:
                ret = cls(1)
            ret.update(**dictionary)
            return ret

    @classmethod
    def load_from_file(cls):
        """gets list of classes form json file"""
        file = str(cls.__name__) + ".json"
        try:
            with open(file, "r") as jsonfile:
                dict_list = Base.from_json_string(jsonfile.read())
                return [cls.create(**i) for i in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save CSV serial to file"""
        file = cls.__name__ + ".csv"
        with open(file, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for ob in list_objs:
                    writer.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """gets CSV deserial from file"""
        file = cls.__name__ + ".csv"
        try:
            with open(file, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(csvfile, fieldnames=fieldnames)
                dict_list = [dict([k, int(v)] for k, v in i.items())
                             for i in dict_list]
                return [cls.create(**i) for i in dict_list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rects and Squares using turtle mod"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#006400")
        turt.pensize(4)
        turt.shape("arrow")
        turt.color("#8B008B")
        for rec in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rec.x, rec.y)
            turt.down()
            for i in range(2):
                turt.forward(rec.width)
                turt.left(90)
                turt.forward(rec.height)
                turt.left(90)
            turt.hideturtle()
        turt.color("#D2691E")
        for sqr in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sqr.x, sqr.y)
            turt.down()
            for i in range(2):
                turt.forward(sqr.width)
                turt.left(90)
                turt.forward(sqr.height)
                turt.left(90)
            turt.hideturtle()
        turtle.exitonclick()
