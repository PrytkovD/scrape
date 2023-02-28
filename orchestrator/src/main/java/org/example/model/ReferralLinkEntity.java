package org.example.model;

import javax.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.SuperBuilder;

@Table(name = "referral_links")
@Entity
@SuperBuilder
@AllArgsConstructor
@NoArgsConstructor
@Data
public class ReferralLinkEntity extends AbstractEntity{

    @ManyToOne
    @JoinColumn(name = "post_id", nullable = false)
    private PostEntity post;

    @Column(name = "link",nullable = false)
    private String link;

    @Column(name = "company_domain", nullable = false)
    private String company;
}
