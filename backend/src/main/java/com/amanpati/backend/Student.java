package com.amanpati.backend;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.List;

@Data
@Document(collection = "students")
public class Student {

    @Id
    private String id;
    private String name;
    private String email;
    private String college;
    private String branch;
    private int year;
    private List<String> skills;
    private String bio;
}