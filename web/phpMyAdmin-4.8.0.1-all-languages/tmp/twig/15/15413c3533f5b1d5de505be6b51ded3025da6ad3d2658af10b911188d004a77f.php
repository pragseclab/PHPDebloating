<?php

/* display/export/options_output_radio.twig */
class __TwigTemplate_ef61516592a72e367698a67da0115e798ab946dc789b5a4aee291269c880aedb extends Twig_Template
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
        echo "<li>
    <input type=\"radio\" id=\"radio_view_as_text\" name=\"output_format\" value=\"astext\"";
        // line 3
        echo (((($context["has_repopulate"] ?? null) || (($context["export_asfile"] ?? null) == false))) ? (" checked") : (""));
        echo ">
    <label for=\"radio_view_as_text\">
        ";
        // line 5
        echo _gettext("View output as text");
        // line 6
        echo "    </label>
</li>
";
    }

    public function getTemplateName()
    {
        return "display/export/options_output_radio.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  29 => 6,  27 => 5,  22 => 3,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "display/export/options_output_radio.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/display/export/options_output_radio.twig");
    }
}
