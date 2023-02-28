package org.example.model;

import javax.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.SuperBuilder;

@Table(name = "comments")
@Entity
@SuperBuilder
@AllArgsConstructor
@NoArgsConstructor
@Data
public class CommentsEntity extends AbstractEntity {

    @Column(name = "all_text", nullable = false)
    private String text;

    @ManyToOne
    @JoinColumn(name = "post_id")
    private PostEntity post;
}
