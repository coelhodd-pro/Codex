from datetime import date

class Note:
    def __init__(self, title, content, name, context, date_created=None):
        self.title = title
        self.content = content
        self.name = name
        self.context = context
        self.date_created = date_created or str(date.today())

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "name": self.name,
            "date": self.date_created,
            "context": self.context
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            content=data["content"],
            name=data["name"],
            context=data["context"],
            date_created=data["date"]
        )

    def summary(self):
        return self.content[:50] + "..." if len(self.content) > 50 else self.content
