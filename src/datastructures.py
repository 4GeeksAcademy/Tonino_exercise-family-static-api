"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
       ]
        

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        self._members.append(member)
        return member

    def delete_member(self, member_id):
        result = list(filter(lambda item: item["id"] == member_id, self._members))
        if result:
            self._members.remove(result[0])
            return {"done": True} 
        else: 
            return "El miembro no existe"

    def get_member(self, member_id):
        result = list(filter(lambda item: item["id"] == member_id, self._members))
        return result[0]

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members