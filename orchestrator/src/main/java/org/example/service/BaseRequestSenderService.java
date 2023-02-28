package org.example.service;

import lombok.RequiredArgsConstructor;
import org.example.config.property.MyRabbitProperties;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZoneOffset;

@Service
@RequiredArgsConstructor
public class BaseRequestSenderService implements RequestSenderService{

    private final RabbitTemplate template;
    private final MyRabbitProperties properties;

    private Instant instant = LocalDateTime.of(2022,1,1,0,0,0).toInstant(ZoneOffset.UTC);

    @Override
    public void sendRequest() {
        template.convertAndSend(
                properties.getExchangeSenderName(),
                properties.getCrawlerRoutingKey(),
                instant
        );
        instant = Instant.now();
    }
}
