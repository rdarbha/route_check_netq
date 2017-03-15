# -- FILE: features/example.feature
Feature: Checking routes

  Scenario: Check routes against last stored routing table
    Given Quagga routing is enabled
     When Routes are being learned
     Then Routes should match our expectations