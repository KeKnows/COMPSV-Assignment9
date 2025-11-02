class Person:
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            friend.add_friend(self)  


class SocialNetwork:
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
        elif person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
        else:
            self.people[person1_name].add_friend(self.people[person2_name])

    def print_network(self):
        for person in self.people.values():
            friends_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friends_names)}")



network = SocialNetwork()

network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")  
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

print("\n--- Social Network ---")
network.print_network()


"""

A social network is best represented using a graph because the relationships between people are not hierarchical or linear. Each person (node) can be connected to any number of other people (edges), and these connections can form complex, overlapping networks. Graphs make it easy to model mutual friendships, shared connections, and paths between users.

A list would not work well because it can only store data sequentially — it doesn’t capture how people are connected to each other. A tree structure is also inappropriate because it enforces a strict parent–child hierarchy, meaning one person could only have one “parent” connection. In contrast, real social networks allow everyone to connect freely, forming cycles and multiple relationships.

From a performance standpoint, using an adjacency list (a dictionary of people where each person has a list of friends) is efficient for most operations. Adding a new person is O(1), and adding a friendship is generally O(1) as well. The main trade-off is that printing or traversing the entire network can become slower as it grows, since you must visit each node and its edges. However, this structure remains flexible, readable, and well-suited to real-world social network modeling.
"""
