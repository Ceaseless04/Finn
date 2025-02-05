package com.finn.server.models;

import org.springframework.data.mongodb.core.mapping.Document;
import jakarta.persistence.Id;

@Document(collection = "users")
public class User {
    @Id
    private String id;
    
    private String email;
    private String password;
}
