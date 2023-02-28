package org.example.config;

import lombok.RequiredArgsConstructor;
import org.example.config.property.MyRabbitProperties;
import org.springframework.amqp.core.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@RequiredArgsConstructor
public class SomeRabbitBeansConfig {

    private final MyRabbitProperties properties;

    @Bean
    public Exchange exchangeReceiver(){
        return ExchangeBuilder
                .directExchange(properties.getExchangeReceiverName())
                .build();
    }

    @Bean
    public Exchange exchangeSender(){
        return ExchangeBuilder
                .directExchange(properties.getExchangeSenderName())
                .build();
    }

    @Bean
    public Queue queueVK(){
        return QueueBuilder
                .durable(properties.getVkRoutingKey())
                .build();
    }

    @Bean
    public Queue queueYoutube(){
        return QueueBuilder
                .durable(properties.getYoutubeRoutingKey())
                .build();
    }

    @Bean
    public Queue queueTelegram(){
        return QueueBuilder
                .durable(properties.getTelegramRoutingKey())
                .build();
    }

    @Bean
    public Binding bindingVK(){
        return BindingBuilder
                .bind(queueVK())
                .to(exchangeReceiver())
                .with(properties.getVkRoutingKey())
                .noargs();
    }

    @Bean
    public Binding bindingTelegram(){
        return BindingBuilder
                .bind(queueTelegram())
                .to(exchangeReceiver())
                .with(properties.getTelegramRoutingKey())
                .noargs();
    }

    @Bean
    public Binding bindingYoutube(){
        return BindingBuilder
                .bind(queueYoutube())
                .to(exchangeReceiver())
                .with(properties.getYoutubeRoutingKey())
                .noargs();
    }

}
