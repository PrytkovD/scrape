package org.example.model;

import javax.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.SuperBuilder;

import java.time.Instant;

@Table(name = "posts")
@Entity
@SuperBuilder
@AllArgsConstructor
@NoArgsConstructor
@Data
public class PostEntity extends AbstractEntity{

    @Column(name = "post_date", nullable = false)
    private Instant postDate;

    @Column(name = "source", nullable = false)
    private String source;

    @ManyToOne
    @JoinColumn(name = "blogger_id", nullable = false)
    BloggerEntity blogger;

    @Column(name = "post_link", nullable = false)
    String link;

    @Column(name = "all_text", nullable = false)
    private String text;

    @Column(name = "comments_count", nullable = false)
    private Long commentsCount;

    @Column(name = "views", nullable = false)
    private Long views;
}
