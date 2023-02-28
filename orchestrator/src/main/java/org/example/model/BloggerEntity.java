package org.example.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.SuperBuilder;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;

@Table(name = "bloggers")
@Entity
@SuperBuilder
@AllArgsConstructor
@NoArgsConstructor
@Data
public class BloggerEntity extends AbstractEntity {

    @Column(name = "channel_name", nullable = false)
    private String channelName;

    @Column(name = "channel_link", nullable = false)
    private String channelLink;

    @Column(name = "followers", nullable = false)
    private Long followers;
}
