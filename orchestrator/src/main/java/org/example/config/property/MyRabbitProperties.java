package org.example.config.property;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.validation.annotation.Validated;

import javax.validation.constraints.NotNull;

@ConfigurationProperties(prefix = "service-rabbit")
@Validated
@Data
public class MyRabbitProperties {
    @NotNull
    private String exchangeReceiverName;

    @NotNull
    private String exchangeSenderName;

    @NotNull
    private String telegramRoutingKey;

    @NotNull
    private String vkRoutingKey;

    @NotNull
    private String youtubeRoutingKey;

    @NotNull
    private String crawlerRoutingKey;
}

