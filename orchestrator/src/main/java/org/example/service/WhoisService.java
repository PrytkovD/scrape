package org.example.service;

import java.util.List;

public interface WhoisService {
    String whois(String domainName);

    List<String> analyze(String text);
}
