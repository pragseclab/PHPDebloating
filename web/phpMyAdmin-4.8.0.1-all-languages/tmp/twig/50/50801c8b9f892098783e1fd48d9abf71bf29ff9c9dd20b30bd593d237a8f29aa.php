<?php

/* config/form_display/group_header.twig */
class __TwigTemplate_f2824e5f0feb3985796244ea01cadc5b55ded3560378f951134a49d71cd7e7b8 extends Twig_Template
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
        echo "<tr class=\"group-header group-header-";
        echo twig_escape_filter($this->env, (isset($context["group"]) ? $context["group"] : null), "html", null, true);
        echo "\">
    <th colspan=\"";
        // line 2
        echo twig_escape_filter($this->env, (isset($context["colspan"]) ? $context["colspan"] : null), "html", null, true);
        echo "\">
        ";
        // line 3
        echo twig_escape_filter($this->env, (isset($context["header_text"]) ? $context["header_text"] : null), "html", null, true);
        echo "
    </th>
</tr>
";
    }

    public function getTemplateName()
    {
        return "config/form_display/group_header.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  28 => 3,  24 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "config/form_display/group_header.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/config/form_display/group_header.twig");
    }
}
