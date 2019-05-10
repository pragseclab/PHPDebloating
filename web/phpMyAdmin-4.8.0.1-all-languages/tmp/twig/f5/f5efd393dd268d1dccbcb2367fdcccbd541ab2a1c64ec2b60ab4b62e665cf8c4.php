<?php

/* display/results/empty_display.twig */
class __TwigTemplate_eccd4d757d2710c372709e409ecc3b6a0b17a7596bc0af03a4175f468509e785 extends Twig_Template
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
        echo twig_escape_filter($this->env, (isset($context["align"]) ? $context["align"] : null), "html", null, true);
        echo " class=\"";
        echo twig_escape_filter($this->env, (isset($context["classes"]) ? $context["classes"] : null), "html", null, true);
        echo "\"></td>
";
    }

    public function getTemplateName()
    {
        return "display/results/empty_display.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "display/results/empty_display.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/display/results/empty_display.twig");
    }
}
