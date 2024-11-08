class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify(self, items):
        return "\n- " + "\n- ".join(items) if items else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:{self._stringify(self.authors)}"
            f"\n\nDependencies:{self._stringify(self.dependencies)}"
            f"\n\nDevelopment dependencies:{self._stringify(self.dev_dependencies)}"
        )
