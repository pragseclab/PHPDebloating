<?php

/* display/results/options_block.twig */
class __TwigTemplate_d534cc12f994ad71c718eb1cebcd0486d78a374f97762b1cd8bf5b95373c0e40 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<form method=\"post\" action=\"sql.php\" name=\"displayOptionsForm\" class=\"ajax print_ignore\">
    ";
        // line 2
        echo PhpMyAdmin\Url::getHiddenInputs(array("db" =>         // line 3
($context["db"] ?? null), "table" =>         // line 4
($context["table"] ?? null), "sql_query" =>         // line 5
($context["sql_query"] ?? null), "goto" =>         // line 6
($context["goto"] ?? null), "display_options_form" => 1));
        // line 8
        echo "

    ";
        // line 10
        echo PhpMyAdmin\Util::getDivForSliderEffect("", _gettext("Options"));
        echo "
        <fieldset>
            <div class=\"formelement\">
                ";
        // line 14
        echo "                ";
        echo PhpMyAdmin\Util::getRadioFields("pftext", array("P" => _gettext("Partial texts"), "F" => _gettext("Full texts")),         // line 20
($context["pftext"] ?? null), true, true, "", ("pftext_" .         // line 24
($context["unique_id"] ?? null)));
        // line 25
        echo "
            </div>

            ";
        // line 28
        if ((($context["relwork"] ?? null) && ($context["displaywork"] ?? null))) {
            // line 29
            echo "                <div class=\"formelement\">
                    ";
            // line 30
            echo PhpMyAdmin\Util::getRadioFields("relational_display", array("K" => _gettext("Relational key"), "D" => _gettext("Display column for relationships")),             // line 36
($context["relational_display"] ?? null), true, true, "", ("relational_display_" .             // line 40
($context["unique_id"] ?? null)));
            // line 41
            echo "
                </div>
            ";
        }
        // line 44
        echo "
            <div class=\"formelement\">
                ";
        // line 46
        $this->loadTemplate("checkbox.twig", "display/results/options_block.twig", 46)->display(array("html_field_name" => "display_binary", "label" => _gettext("Show binary contents"), "checked" =>  !twig_test_empty(        // line 49
($context["display_binary"] ?? null)), "onclick" => false, "html_field_id" => ("display_binary_" .         // line 51
($context["unique_id"] ?? null))));
        // line 53
        echo "                ";
        $this->loadTemplate("checkbox.twig", "display/results/options_block.twig", 53)->display(array("html_field_name" => "display_blob", "label" => _gettext("Show BLOB contents"), "checked" =>  !twig_test_empty(        // line 56
($context["display_blob"] ?? null)), "onclick" => false, "html_field_id" => ("display_blob_" .         // line 58
($context["unique_id"] ?? null))));
        // line 60
        echo "            </div>

            ";
        // line 66
        echo "            <div class=\"formelement\">
                ";
        // line 67
        $this->loadTemplate("checkbox.twig", "display/results/options_block.twig", 67)->display(array("html_field_name" => "hide_transformation", "label" => _gettext("Hide browser transformation"), "checked" =>  !twig_test_empty(        // line 70
($context["hide_transformation"] ?? null)), "onclick" => false, "html_field_id" => ("hide_transformation_" .         // line 72
($context["unique_id"] ?? null))));
        // line 74
        echo "            </div>

            <div class=\"formelement\">
                ";
        // line 77
        echo PhpMyAdmin\Util::getRadioFields("geoOption", array("GEOM" => _gettext("Geometry"), "WKT" => _gettext("Well Known Text"), "WKB" => _gettext("Well Known Binary")),         // line 84
($context["geo_option"] ?? null), true, true, "", ("geoOption_" .         // line 88
($context["unique_id"] ?? null)));
        // line 89
        echo "
            </div>

            <div class=\"clearfloat\"></div>
        </fieldset>

        <fieldset class=\"tblFooters\">
            <input type=\"submit\" value=\"";
        // line 96
        echo _gettext("Go");
        echo "\" />
        </fieldset>
    </div>";
        // line 99
        echo "</form>
";
    }

    public function getTemplateName()
    {
        return "display/results/options_block.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  109 => 99,  104 => 96,  95 => 89,  93 => 88,  92 => 84,  91 => 77,  86 => 74,  84 => 72,  83 => 70,  82 => 67,  79 => 66,  75 => 60,  73 => 58,  72 => 56,  70 => 53,  68 => 51,  67 => 49,  66 => 46,  62 => 44,  57 => 41,  55 => 40,  54 => 36,  53 => 30,  50 => 29,  48 => 28,  43 => 25,  41 => 24,  40 => 20,  38 => 14,  32 => 10,  28 => 8,  26 => 6,  25 => 5,  24 => 4,  23 => 3,  22 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "display/results/options_block.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/display/results/options_block.twig");
    }
}
