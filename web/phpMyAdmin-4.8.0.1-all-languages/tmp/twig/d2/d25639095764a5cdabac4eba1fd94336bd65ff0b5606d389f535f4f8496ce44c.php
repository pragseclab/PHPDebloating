<?php

/* display/results/null_display.twig */
class __TwigTemplate_2ddd29ecc5b81ef2c0ddd189841378c8e727630b678563e085af41d165e8217d extends Twig_Template
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
        echo "<td ";
        echo twig_escape_filter($this->env, ($context["align"] ?? null), "html", null, true);
        echo "
    data-decimals=\"";
        // line 2
        echo twig_escape_filter($this->env, (($this->getAttribute(($context["meta"] ?? null), "decimals", array(), "any", true, true)) ? ($this->getAttribute(($context["meta"] ?? null), "decimals", array())) : ("-1")), "html", null, true);
        echo "\"
    data-type=\"";
        // line 3
        echo twig_escape_filter($this->env, $this->getAttribute(($context["meta"] ?? null), "type", array()), "html", null, true);
        echo "\"
    ";
        // line 5
        echo "    class=\"";
        echo twig_escape_filter($this->env, ($context["classes"] ?? null), "html", null, true);
        echo " null\">
    <em>NULL</em>
</td>
";
    }

    public function getTemplateName()
    {
        return "display/results/null_display.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  32 => 5,  28 => 3,  24 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "display/results/null_display.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/display/results/null_display.twig");
    }
}
