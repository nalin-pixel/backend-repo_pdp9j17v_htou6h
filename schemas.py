"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class WeddingInquiry(BaseModel):
    """
    Wedding inquiries submitted by couples
    Collection name: "weddinginquiry"
    """
    bride_name: str = Field(..., description="Bride or Partner A full name")
    groom_name: str = Field(..., description="Groom or Partner B full name")
    email: EmailStr = Field(..., description="Primary contact email")
    phone: Optional[str] = Field(None, description="Contact phone number")
    wedding_date: Optional[str] = Field(None, description="Preferred wedding date (YYYY-MM-DD)")
    venue: Optional[str] = Field(None, description="Venue or city")
    guest_count: Optional[int] = Field(None, ge=1, description="Estimated number of guests")
    budget_range: Optional[str] = Field(None, description="Estimated budget range")
    services: Optional[List[str]] = Field(default_factory=list, description="Services interested in")
    message: Optional[str] = Field(None, description="Additional details or notes")
