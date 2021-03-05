import arcade


class ActorManager:
    """
    Holds all of the actors and manages adding and removing them from the scene
    """

    def __init__(self):
        self.actors = arcade.SpriteList()

    def remove_actor(self, actor):
        """
            removes actor from list
        :param actor: actor to remove
        """
        self.actors.remove(actor)

    def add_actor(self, actor):
        """
            adds actor to list
        :param actor: actor to add
        """
        self.actors.append(actor)

    def add_actor_list(self, actors: arcade.SpriteList):
        """
            takes a sprite list and adds those sprites to self.actors
        :param actors: spritelist to be added
        """
        for actor in actors:
            self.actors.append(actor)