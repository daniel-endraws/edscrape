from . import BASE_URL

class User():
  """
  Represents the information from the ed user api
  """

  def __init__(self, data: dict) -> None:
    self.courses: list[Course] = list(map(Course, data["courses"]))
    self.active_courses: list[Course] = list(filter(lambda c: c.is_active, self.courses))
    user = data["user"]
    self.id: int = int(user["id"])
    self.name: str = user["name"]
    self.email: str = user["email"]

  def get_course(self, course_id: int) -> "Course":
    res = [c for c in self.courses if c.id == course_id]
    return res[0] if len(res) else None
    

class Course():
  """
  Represents a course, containing information about the course 
  """

  def __init__(self, data: dict) -> None:
    course = data["course"]
    role = data["role"]

    self.id: int = int(course["id"])
    self.code: str = course["code"]
    self.name: str = course["name"]
    self.year: int = int(course["year"]) if course["year"] != "X" else None
    self.session: str = course["session"] if course["session"] != "X" else None
    self.is_active: bool = course["status"] == "active"

    self.user_id: int = int(role["user_id"])
    self.role: str = role["role"]
    