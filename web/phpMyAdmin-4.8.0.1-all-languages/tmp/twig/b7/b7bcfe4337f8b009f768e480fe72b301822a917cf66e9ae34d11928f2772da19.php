<?php

/* columns_definitions/column_length.twig */
class __TwigTemplate_92249374b44429b4ba3bc4ffff0ef5eab4c8f7aa7f85d348794bed8ab2237647 extends Twig_Template
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
        echo "<input id=\"field_";
        echo twig_escape_filter($this->env, (isset($context["column_number"]) ? $context["column_number"] : null), "html", null, true);
        echo "_";
        echo twig_escape_filter($this->env, ((isset($context["ci"]) ? $context["ci"] : null) - (isset($context["ci_offset"]) ? $context["ci_offset"] : null)), "html", null, true);
        echo "\"
    type=\"text\"
    name=\"field_length[";
        // line 3
        echo twig_escape_filter($this->env, (isset($context["column_number"]) ? $context["column_number"] : null), "html", null, true);
        echo "]\"
    size=\"";
        // line 4
        echo twig_escape_filter($this->env, (isset($context["length_values_input_size"]) ? $context["length_values_input_size"] : null), "html", null, true);
        echo "\"
    value=\"";
        // line 5
        echo twig_escape_filter($this->env, (isset($context["length_to_display"]) ? $context["length_to_display"] : null), "html", null, true);
        echo "\"
    class=\"textfield\" />
<p class=\"enum_notice\" id=\"enum_notice_";
        // line 7
        echo twig_escape_filter($this->env, (isset($context["column_number"]) ? $context["column_number"] : null), "html", null, true);
        echo "_";
        echo twig_escape_filter($this->env, ((isset($context["ci"]) ? $context["ci"] : null) - (isset($context["ci_offset"]) ? $context["ci_offset"] : null)), "html", null, true);
        echo "\">
    <a href=\"#\" class=\"open_enum_editor\">
        ";
        // line 9
        echo _gettext("Edit ENUM/SET values");
        // line 10
        echo "    </a>
</p>
";
    }

    public function getTemplateName()
    {
        return "columns_definitions/column_length.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  49 => 10,  47 => 9,  40 => 7,  35 => 5,  31 => 4,  27 => 3,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "columns_definitions/column_length.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/columns_definitions/column_length.twig");
    }
}
