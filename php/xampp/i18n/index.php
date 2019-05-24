<?php

// $language = ["en_US", "en_US.UTF-8", "en-US", "en-US.UTF-8"];
// $language = ["tr_TR", "tr-TR", "tr", "tr_TR.UTF-8", "tr-TR.UTF-8", "tr.UTF-8"];
$language = ["nl_NL", "nl_NL.UTF-8", "nl-NL", "nl-NL.UTF-8"];

putenv("LANG=" . $language[0]);
$locale = setlocale(LC_ALL, $language);

$domain = "messages";
bindtextdomain($domain, "locales"); 
bind_textdomain_codeset($domain, "UTF-8");
textdomain($domain);

if (!defined("LC_MESSAGES")) {
    echo "<p>LC_MESSAGES is NOT defined.</p>";
}

if (!function_exists("gettext")) {
    echo "<p>gettext() does not exist.</p>";
}

echo "<p>" . $locale . "</p>";
echo "<p>" . _("title") . "</p>";
echo "<p>" . _("content") . "</p>";
