# Example usage:
data = {
    "agent_id": "A001",
    "agent_code": "abcd",
    "first_name": "Nimal",
    "last_name": "Perera",
    "email": "nimalperera@gmail.com",
    "phone": "0769024567",
    "branch_id": "123e4567-e89b-12d3-a456-426614174000",
    "created_at": "2025-03-29 15:07:05",
    "updated_at": "2025-03-29 15:07:05"
}

agent = Agent(**data)
print(agent)