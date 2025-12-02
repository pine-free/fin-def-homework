from pydantic import BaseModel

class Case(BaseModel):
    num_claims: int
    guilty: str
    victim: str

    @staticmethod
    def __get_short_name(full_name: str) -> str:
        surname, name, patr = full_name.split()
        return f"{surname} {name[0].capitalize()}. {patr[0].capitalize()}."
    
    @property
    def guilty_initials(self):
        return self.__get_short_name(self.guilty)
    
    @property
    def victim_initials(self):
        return self.__get_short_name(self.victim)